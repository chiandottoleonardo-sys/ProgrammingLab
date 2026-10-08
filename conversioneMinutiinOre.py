minuti_totali = 538

ore = minuti_totali / 60

int_ore = int(ore)

minuti = minuti_totali % 60

print(f"{int_ore}h:{minuti}min")