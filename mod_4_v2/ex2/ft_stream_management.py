import sys

def function():
	id = input("enter id: ")
	print(f"id = {id}", file=sys.stdout)
	print(f"erro chanel", file=sys.stderr)

if __name__ == "__main__":
	function()
