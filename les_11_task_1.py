def count_points(win: int, draw: int, loss: int) -> int:
    """The score of football matches"""
    return win * 3 + draw * 1 + loss * 0


print(count_points(3, 2, 2))
