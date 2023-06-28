class teacherAtCodingal:
    def __init__(self, name, language, country):
        self.name = name
        self.language = language
        self.country = country
        
    def __str__(self) -> str:
        return f"Hi i am {self.name}, I write code in {self.language}. I am from {self.country}"
    
    def sayHello(self):
        return f"Hi i am {self.name}"
    
    def __del__(self):
        return f"deleted"
    
    
Fahim = teacherAtCodingal("Fahim","python","BD")

print(Fahim)