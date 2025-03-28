marks = {
    "vaibhav": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "vaibhav"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"vaibhav": 99, "Renuka": 100})
# print(marks)

print(marks.get("vaibhav2")) # Prints None
print(marks["vaibhav2"]) # Returns an error