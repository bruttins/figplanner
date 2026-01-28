def display_schedule(rounds, names):
    print("\n" + "=" * 80)
    print("TRAININGSPLAN")
    print("=" * 80)

    max_width = 10
    for name in names:
        if len(name) > max_width:
            max_width = len(name) + 1
    padding = max_width + 11

    print(f"\n{'Runde':<10} {'Figurant 1':<{max_width}} "
          f"{'Hund':<{max_width}} {'Figurant 2':<{max_width}}")
    print(f"{'':<{padding}} {'Mitte':<{max_width}}")
    print("-" * 80)

    for i, round_data in enumerate(rounds, 1):
        print(f"\n{i:<10} {round_data['fig1']:<{max_width}} "
              f"{round_data['trainee']:<{max_width}} {round_data['fig2']:<{max_width}}")
        print(f"{'':<{padding}} {round_data['observer']:<{max_width}}")
    print("-" * 80)