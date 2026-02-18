class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm):
        self.height += cm

    def age_plant(self, days):
        self.age += days

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age}days old"

def main():
    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    rose.display_info()
    sunflower.display_info()
    cactus.display_info()

if __name__ == "__main__":
    main()
