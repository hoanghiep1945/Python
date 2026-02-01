with open("CONTACT.in", "r", encoding="utf-8") as f:
    emails = [line.strip().lower() for line in f if line.strip()]

emails = sorted(set(emails))

for e in emails:
    print(e)