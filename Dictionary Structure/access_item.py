student_information = {
    "std_id1" : {"Name" : "Md. Jahanggir Alom", "District" : "Dinajpur"},
    "std_id2" : {"Name" : "Mst. Mim Akter", "District" : "Rangpur"},
    "std_id3" : {"Name" : "Md. Foridul Islam", "District" : "Rangpur"},
    "std_id4" : {"Name" : "Sumon Roy", "District" : "Nilfamari"},
    "std_id5" : {"Name" : "Mst. Aporna Akter", "District" : "Dinajpur"}
}

print(student_information["std_id2"])
print(student_information["std_id4"]['Name'])
print(student_information["std_id4"]["District"])
