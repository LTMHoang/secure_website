def count_course(course):
    total_amount, total_quantity = 0, 0

    if course:
        for c in course.values():
            total_quantity += c['quantity']
            total_amount = c['quantity']

    return {
        "total_amount": total_amount,
        "total_quantity": total_quantity
    }
