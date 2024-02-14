#include <iostream>
#include <cmath>

using std::cin;
using std::cout;
using std::string;

int main()
{

    // Obtendo as informações do usuário

    double temperatura_original;
    char unidade_original;
    double temperatura_convertida;

    cout << "Qual a temperatura? \n";
    cin >> temperatura_original;

    cout << "Em que unidade esta essa temperatura ('C' para Célsius / 'F' para Farenheit)? \n";
    cin >> unidade_original;

    // Realizando as conversões

    switch (unidade_original)
    {
    case 'C':
        // Caso a temperatura original for Celcius, converter para Farenheit

        temperatura_convertida = (1.8 * temperatura_original) + 32;
        cout << "A temperatura convertida para " << unidade_original << "° e de " << round(temperatura_convertida) << " graus.\n";

        break;
    case 'F':
        // Caso a temperatura original for Farenheit, converter para Celcius

        temperatura_convertida = (temperatura_original - 32) / 1.8;
        cout << "A temperatura convertida para " << unidade_original << "° e de " << round(temperatura_convertida) << " graus.\n";

        break;

    default:
        // Caso a unidade seja diferente de C ou F

        cout << "Nao foi possivel converter, unidade nao reconhecida.\n";
        break;
    }

    return 0;
}
