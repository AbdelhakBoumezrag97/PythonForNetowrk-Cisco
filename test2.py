Devcie_List=["R1 2911","R2 2811","R3 900","Catalyst 9200","Catalyst 2650"]

Catalyst_Switch_List=[]
for item in Devcie_List:
	if "Catalyst" in item: Catalyst_Switch_List.append(item)
	print(Catalyst_Switch_List)

	
