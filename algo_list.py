def print_comb() -> None:
    for i in range(8):
        for j in range(9):
            for k in range(10):
                if i < j and j < k:
                    print(f"{i}{j}{k}")

print_comb()