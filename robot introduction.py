# 🌟✨ ROBOT INTRODUCTION USING OOP ✨🌟

# 🧠 Class to define your robot
class Robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    # 💬 Method to introduce the robot
    def introduce(self):
        print(f"🤖 Hello! I am {self.name}.")
        print(f"🔧 Model: {self.model}")
        print(f"🎯 My purpose is: {self.purpose}")
        print("💡 I am powered by Python and imagination!")

# 🌈 Create a cute robot object
my_robot = Robot(
    name="TulipBot 🌷", 
    model="TLP-2025", 
    purpose="Helping with homework in a cute way!"
)

# 🗣️ Let the robot speak!
my_robot.introduce()
