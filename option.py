def option(question, option_count, *rest):
	n = 0
	if option_count != len(*rest):
		return 1
	else:
        print(f"question")
        for i in range(option_count):
            print(f"{i}. {rest[i]}")
        return ans = int(input("Enter your choice: "))