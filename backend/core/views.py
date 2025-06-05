from django.shortcuts import render
from .agent import create_agent
from .utils import get_db, save_log, hash_file_content
import csv
from datetime import datetime

agent_instance = None
filename = None

def home(request):
    global agent_instance, filename
    answer = None

    if request.method == "POST":
        if "csv_file" in request.FILES:
            file = request.FILES["csv_file"]
            file_data = file.read()
            hash_val = hash_file_content(file_data)

            db = get_db()
            files_collection = db["agent_age"]
            existing_file = files_collection.find_one({"type": "csv", "hash": hash_val})

            if existing_file:
                answer = f"⚠️ File '{file.name}' already exists in MongoDB."
                csv_content = existing_file.get("raw")
                if not csv_content:
                    # fallback to reconstructing CSV from rows (if raw not stored)
                    import io
                    import csv
                    if "data" in existing_file:
                        output = io.StringIO()
                        writer = csv.DictWriter(output, fieldnames=existing_file["data"][0].keys())
                        writer.writeheader()
                        writer.writerows(existing_file["data"])
                        csv_content = output.getvalue()
                    else:
                        answer = "❌ Error: CSV content not found in DB."
                        return render(request, "home.html", {"answer": answer})

                agent_instance = create_agent(csv_content)
            else:
                decoded = file_data.decode("utf-8")
                csv_reader = csv.DictReader(decoded.splitlines())
                rows = list(csv_reader)

                files_collection.insert_one({
                    "type": "csv",
                    "filename": file.name,
                    "hash": hash_val,
                    "raw": decoded,  # ✅ store raw string
                    "data": rows,
                    "timestamp": datetime.now()
                })

                answer = f"✅ Uploaded '{file.name}' to MongoDB"
                agent_instance = create_agent(decoded)


        elif "question" in request.POST:
            question = request.POST["question"]
            if agent_instance:
                answer = agent_instance.invoke(question)
                try:
                    save_log(question, answer, filename)
                except Exception as e:
                    print("⚠️ MongoDB log failed:", e)

    # ✅ Make sure to always return an HttpResponse!
    return render(request, "home.html", {"answer": answer})
