def tri_count(n):
	count = 0
	for a in range(n+1):
		for b in range(n+1):
			for c in range(n+1):
				for d in range(n+1):
					x = ((a**2)+(b**2))**0.5
					y = ((c**2)+(d**2))**0.5
					z = ((a-c)**2+(b-d)**2)**0.5
					side_list = [x,y,z]
					side_list.sort()
					if round((side_list[0])**2,2) + round((side_list[1])**2,2) == round((side_list[2])**2) and side_list[0]+side_list[1]>side_list[2]:
						count += 1
	return int(count/2)

print(tri_count(50))
