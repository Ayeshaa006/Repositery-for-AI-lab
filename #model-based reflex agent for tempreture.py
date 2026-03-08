#model-based reflex agent for tempreture control system
class tempretureAgent:
    def __init__(self, desired_temp=22):
        self.desired_temp = desired_temp
        self.heater_status = "off"
    def act(self, current_temp):
        print(f"current_temp: {current_temp} | heater is: {self.heater_status}")
        if current_temp < self.desired_temp:
            if self.heater_status == "off":
                self.heater_status = "on"
                return "action: turning heater on"
            else:
                return "action: no change (heater is already on)"
        else:
            if self.heater_status == "on":
                self.heater_status = "off"
                return "action: turning heater off"
            else:
                return "action: no change (heater is already off)"

agent = tempretureagent(desired_temp=20)
room_tempreture = [18, 17, 19, 21, 22, 20]
print("---starting model-based reflex agent---")
for temp in room_tempretures:
    result = agent.act(temp)
    print(result)
    print("-" * 10)
    