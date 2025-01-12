def generate_recommendations(expenses_by_category, income):
    recommendations = []

    # Set dining_expense to 0 if 'Dine-outs' is not found in expenses_by_category
    dining_expense = expenses_by_category.get('Dine-outs', 0)
    if dining_expense > 3000:
        recommendations.append("Consider subscribing to Zomato Gold to save on dining expenses. You spend over 3000 per month on dining so you would save more with a subscription.")

    wants_categories = ['Dine-Outs', 'Entertainment', 'Shopping']
    total_wants = sum(expenses_by_category.get(category, 0) for category in wants_categories)
    if total_wants > income * 0.30:
        recommendations.append("Your discretionary expenses exceed the recommended 30% of your income. Consider cutting back on dining out, shopping, or entertainment.")

    health_expense = expenses_by_category.get('Health & Fitness', 0)
    if health_expense > 2000:
        recommendations.append("Consider a gym membership or fitness program to make the most of your health-related spending.")

    if not recommendations:
        recommendations.append("You're managing your expenses well! Keep up the good work.")

    return recommendations
