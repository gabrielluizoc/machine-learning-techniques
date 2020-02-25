import csv
import matplotlib.pyplot as plt 
import math

# Linear Regression Y = α X + β + error
# R² = (Σxi.yi - Σxi.Σyi / n) / √ Σxi² - ((Σxi)² / 5) * ((Σyi)² / 5)
# α: Dependent Coefficient
# β: Coeficiente Independente

# α = n*(Σxi*yi) - Σxi*Σyi / n*Σxi² - (Σxi)²
# β = (y / n) - (α*x) / n

IR = []
CHR = []

with open('./data.csv') as csvfile:
    csvfile = csv.DictReader(csvfile)
    for row in csvfile:
        IR.append(row['illiteracy_rate'])
        CHR.append(row['child_mortality_rate'])
    IR = list(map(float, IR))
    CHR = list(map(float, CHR))

print('Illiteracy Rate(x): ',IR)
print('Child Mortality Rate(y): ',CHR)

def linear_regression(x, y):
    # Linear Regression
    linearReg = 0
    # α: Dependent Coefficient
    dependentCoe = 0
    # β: Coeficiente Independente
    independetCoe = 0

    ## Sum of variables

    # Σxi
    sumX = sum(x)
    # Σyi
    sumY = sum(y)

    # Sample size
    sampleSize = len(x)
    
    # Multiplication counter
    count = 0

    # Multiplied samples array and Multiplied value of temporary samples    
    multipliedSamples = []
    multipliedSample = 0    

    # Multiplication of variables
    while(count < sampleSize):
        multipliedSample = x[count] * y[count]
        multipliedSamples.append(round(multipliedSample, 2))
        count += 1
    
    # Sum of multiplications
    sumMultiplication = round(sum(multipliedSamples), 2)

    # Variable x squared
    xSquareds = []    
    
    for num in x:
        squared = 0
        squared += (num ** 2)
        xSquareds.append(round(squared, 2))
    
    # Sum of numbers X squareds
    sumXSquared = round(sum(xSquareds), 2)

    # Variable Y squared
    ySquareds = []    
    
    for num in y:
        squared = 0
        squared += (num ** 2)
        ySquareds.append(round(squared, 2))
    
    # Sum of numbers X squareds
    sumYSquared = round(sum(ySquareds), 2)

    # Sum of α
    dependentCoe = round(((sampleSize * sumMultiplication) - (sumX * sumY)) / ((sampleSize * sumXSquared) - (sumX ** 2)), 2)    

    # Sum of β
    independetCoe = round(((sumY / sampleSize) - (dependentCoe * (sumX / sampleSize))), 2)

    # Linear Regressions    
    linearReg = round(((dependentCoe * 59) + independetCoe), 2)
    linearRegs = []
    for num in x:
        linearRegs.append(round(((dependentCoe * num) + independetCoe), 2))

    # Sum of R²
    correlation_coe = round((sumMultiplication - ((sumX * sumY) / sampleSize)) / math.sqrt((sumXSquared - ((sumX ** 2) / sampleSize)) * (sumYSquared - ((sumY ** 2) / sampleSize))), 2)
    
    # Outputs
    print('Σxi: ',sumX)
    print('Σyi: ', sumY)
    print('ΣxiΣyi: ',sumMultiplication)
    print('Σxi²: ',sumXSquared)
    print('Σyi²: ',sumYSquared)
    print('α: ',dependentCoe)
    print('β: ',independetCoe)
    print('Linear Regression Defined: ',linearReg)
    print('Linear Regressions: ',linearRegs)
    print('R²: ',correlation_coe)

    plt.scatter(x,y)
    plt.plot(x, linearRegs, color = 'red', linewidth = 3)
    plt.title('Linear Regression')
    plt.xlabel('Illiteracy Rate')
    plt.ylabel('Child Mortality Rate')
    plt.show()

linear_regression(IR, CHR)