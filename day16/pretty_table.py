from prettytable import PrettyTable

#create new object
table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"
print(table)