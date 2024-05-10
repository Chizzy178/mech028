def roles_of_astronauts(**kw):
    for key, value in kw.items():
        return f"{key} : {value}" 
    return f"These are the {len(kw)} astronauts on this mission"
   
print(roles_of_astronauts(Commander = "Solomon", Pilot = "Joshua", Maintenance = "Jackie"))
