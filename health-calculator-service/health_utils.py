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
        height: Taille en mètres
        age: Âge en années
        gender: Genre ('male' ou 'female')
        
    Returns:
        float: BMR en calories par jour
    """
    if gender.lower() not in ['male', 'female']:
        raise ValueError("Le genre doit être 'male' ou 'female'.")
    
    # Conversion de la taille de mètres en centimètres
    height_cm = height * 100
    
    if gender.lower() == 'male':
        # Formule ajustée pour les hommes
        bmr = 88.362 + (13.397 * weight) + (4.799 * height_cm) - (5.677 * age)
    else:
        # Formule ajustée pour les femmes
        bmr = 447.593 + (9.247 * weight) + (3.098 * height_cm) - (4.330 * age)
    
    return round(bmr, 2)