class PlayerCharacter:
    
    def __init__(self, health, armorRating, attackPower):
        self.__health = health
        self.__armorRating = armorRating
        self.__attackPower = attackPower
    def set_health(self, health):
        self.__health = health
    def set_armor_rating(self, armorRating):
        self.__armorRating = armorRating
    def set_attack_power(self, attackPower):
        self.__attackPower = attackPower
    def get_health(self):
        return self.__health
    def get_armor_rating(self):
        return self.__armorRating
    def get_attack_power(self):
        return self.__attackPower
    
    def __str__(self):
        return f'Player Health: {self.__health}' + f'\nPlayer Armor: {self.__armorRating}' + f'\nPlayer Attack Power: {self.__attackPower}' 


def healthPrompt():
    playerHealth = int(input('Enter player health (1-100): '))
    if 1 <= playerHealth <= 100:
        return playerHealth
    else:
        print('Value outside of range')
        healthPrompt()

def armorPrompt():
    playerArmor = int(input('Enter player armor (1-20): '))
    if 1 <= playerArmor <= 20:
        return playerArmor
    else:
        print('Value outside of range')
        armorPrompt()

def attackPrompt():
    playerAttack = int(input('Enter player attack (1-20): '))
    if 1 <= playerAttack <= 20:
        return playerAttack
    else:
        print('Value outside of range')
        attackPrompt()

        
def main():

    print("Welcome to Jae's RPG")

    playerHealth = healthPrompt()
    playerArmor = armorPrompt()
    playerAttack = attackPrompt()
    
    Wizard = PlayerCharacter(playerHealth, playerArmor, playerAttack)
    print(Wizard)


if __name__ == "__main__":
    
    main()