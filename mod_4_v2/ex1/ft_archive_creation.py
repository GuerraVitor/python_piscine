def ft_archive_creation():
	archive = open("new_discovery.txt", "w")
	archive.write("New quantum algorithm discovered")
	archive.close()

	archive = open("new_discovery.txt", "r")
	content = archive.read()
	print(content)
	archive.close()

if __name__ == "__main__":
	ft_archive_creation()
