phone = "082611531020"
masked = phone[:4] + "*" * 5 + phone[-3:]
print(masked)