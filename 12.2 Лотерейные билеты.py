from random import choice
import string
tickets = set()
while len(tickets) < 100:
    ticket = ''
    for _ in range(7):
        ticket += str(choice(string.digits))
    if ticket not in tickets and ticket[0] != '0':
                     print(ticket)
                     tickets.add(ticket)
