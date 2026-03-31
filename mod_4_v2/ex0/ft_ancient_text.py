def ft_ancient_text():
	info = open("ancient_fragment.txt", "r")
	content = info.read()
	print(content)

	info.close()


if __name__ == "__main__":
	ft_ancient_text()
