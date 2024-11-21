# health_utils.py

def calculate_bmi(weight: float, height: float) -> float:
    """Calculer l'Indice de Masse Corporelle (BMI)."""
    if height <= 0:
        raise ValueError("La hauteur doit être supérieure à zéro.")
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def calculate_bmr(weight: float, height: float, age: int, gender: str) -> float:
    """Calculer le Taux Métabolique de Base (BMR).
    
    Args:
        weight: Poids en kg
        height: Taille en cm
        age: Âge en années
        gender: Genre ('male' ou 'female')
        
    Returns:
        float: BMR en calories par jour
    """
    if gender.lower() not in ['male', 'female']:
        raise ValueError("Le genre doit être 'male' ou 'female'.")
    
    if gender.lower() == 'male':
        # Formule de Mifflin-St Jeor pour les hommes
        bmr = 66.47 + (13.75 * weight) + (5.0033 * height) - (6.755 * age)
    else:
        # Formule de Mifflin-St Jeor pour les femmes
        bmr = 655.1 + (9.563 * weight) + (1.8496 * height) - (4.6756 * age)
    
    return round(bmr, 2)