import os
import sys


def main_menu():
    while 1:
        print('=============================================')
        print('---------------Easy Attack v1----------------')
        print('\nchoose an option...')
        print('1: set network interface')
        print('2: set attack type')
        print('3: set victim ip')
        print('4: Execute Attack')
        print('5: exit easy attack')
        print('=============================================')
        command = raw_input('Enter an option >>> ')
        if command == '1':
        elif command == '2':
            attack = attack_menu()
        elif command == '3':
            ip = raw_input('Enter victim ip')
        elif command == '4':
            if attack == '':
                print('No attack selected... opening attack menu')
                attack = attack_menu()
        elif command == '5':
            exit()

def attack_menu():
    while 1:
        print('//////////////////////////////////////////')
        print('---------------ATTACK MENU----------------')
        print('\nchoose an option...')
        print('1: DOS options')
        print('2: ARP Poisoning')
        print('3: DNS Poisoning')
        print('4: Go Back To Main Menu')
        print('//////////////////////////////////////////')
        command = raw_input('(ATTACK) Enter an option >>> ')
        if command == '1':
            dos_menu()


def dos_menu():
    while 1:
        print('//////////////////////////////////////////')
        print('---------------ATTACK MENU----------------')
        print('\nchoose an option...')
        print('1: DOS options')
        print('2: ARP Poisoning')
        print('3: DNS Poisoning')
        print('4: Go Back To Main Menu')
        print('//////////////////////////////////////////')
        command = raw_input('(ATTACK) Enter an option >>> ')
        if command == '1':
            dos_menu()
def arp_menu():
def dns_menu():

if __name__ == '__main__':
    main_menu():
        


