"""
This module handle reduce app
 
Functions: reduce(alpha, beta)
"""
def reduce(variable_alpha, variable_beta):
    """Takes in two numbers, returns their product."""
    return variable_alpha + variable_beta

def app():
    """Run the app."""
    print('hello we reduced to :', reduce(1, 2))

if __name__=="__main__":
    """Main loop."""
    app()
