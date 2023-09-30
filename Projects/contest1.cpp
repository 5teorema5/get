#include <iostream>
using namespace std;
struct Crystal
{
    double length;            // длина кристалла
    double width;             // характерная толщина кристалла
    unsigned int facets;      // количество граней
    unsigned long int color;  // код цвета
    unsigned int defects;     // количество дефектов
};
struct Category
{
    char name[100];                          // название категории
    double length_min, length_max;           // допустимая длина кристалла
    double width_min, width_max;             // допустимая характерная толщина кристалла
    unsigned int facets_min, facets_max;     // допустимое количество граней
    unsigned long int colors[5];             // допустимые коды цвета
    unsigned int defects_min, defects_max;   // допустимое количество дефектов
};
Category categories[10];
int determine_category(Crystal crystal) {
    for (int i = 0; i < 10; i++) {
        Category a = categories[i];
        bool flag = false;
        for (int j = 0; j < 5; j++) {
            if (crystal.color == a.colors[j]) {
                flag = true;
                break;
            }
        }
        if ((crystal.length >= a.length_min) and 
        (crystal.length <= a.length_max) and 
        (crystal.width >= a.width_min) and 
        (crystal.width <= a.width_max) and 
        (crystal.facets >= a.facets_min) and 
        (crystal.facets <= a.facets_max) and 
        (crystal.defects >= a.defects_min) and 
        (crystal.defects <= a.defects_max) and flag)
            return i;
    }
    return (-1);
}

int main()
{
    for (int i = 0; i < 10; i++)
    {
        cin >> categories[i].name >> categories[i].length_min >> categories[i].length_max >> categories[i].width_min >> categories[i].width_max >> categories[i].facets_min >> categories[i].facets_max;
        for (int j = 0; j < 5; j++)
            cin >> categories[i].colors[j];
        cin >> categories[i].defects_min >> categories[i].defects_max;
    }
    int n;
    cin >> n;
    int quantities[10] = {0};
    for (int i = 0; i < n; i++)
    {
        Crystal crystal;
        cin >> crystal.length >> crystal.width >> crystal.facets >> crystal.color >> crystal.defects;
        int category = determine_category(crystal);
        if (category < 0 || category > 9)
            continue;
        quantities[category]++;
    }
    for (int i = 0; i < 10; i++)
        cout << quantities[i] << " ";
    cout << endl;
    return 0;
}