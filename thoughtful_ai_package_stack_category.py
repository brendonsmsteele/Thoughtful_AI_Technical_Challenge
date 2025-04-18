
from enum import Enum

class StackCategory(Enum):
    STANDARD = "STANDARD"
    REJECTED = "REJECTED"
    SPECIAL = "SPECIAL"

def packageIsBulky(width: float, height: float, length: float) -> bool:
    return (width * height * length > 1000000) or width > 150 or height > 150 or length > 150

def packageIsHeavy(mass: float) -> bool:
    return mass > 20

def getPackageStackCategory(width: float, height: float, length: float, mass: float) -> str:
    bulky = packageIsBulky(width, height, length)
    heavy = packageIsHeavy(mass)

    if(not bulky and not heavy):
        return StackCategory.STANDARD.value
    elif(bulky and heavy):
        return StackCategory.REJECTED.value
    else:
        return StackCategory.SPECIAL.value
    

def testBulkyPackageWidth():
    assert packageIsBulky(151,20,20) == True

def testBulkyPackageHeight():
    assert packageIsBulky(20,151,20) == True

def testBulkyPackageLength():
    assert packageIsBulky(20,20,151) == True

def testBulkyPackageAll():
    assert packageIsBulky(150,150,150) == True

def testNotBulkyPackage():
    assert not packageIsBulky(10,10,10) 

def testHeavyPackage():
    assert packageIsHeavy(30) == True

def testNotHeavyPackage():
    assert not packageIsHeavy(10)

def testStandardPackage():
    assert getPackageStackCategory(10, 10, 10, 10) == StackCategory.STANDARD.value

def testRejectedPackage():
    assert getPackageStackCategory(150, 150, 150, 30) == StackCategory.REJECTED.value

def testSpecialPackageBulky():
    assert getPackageStackCategory(150, 150, 150, 10) == StackCategory.SPECIAL.value

def testSpecialPackageHeavy():
    assert getPackageStackCategory(10, 10, 10, 30) == StackCategory.SPECIAL.value


def main():
    print("main")

    testBulkyPackageWidth()
    testBulkyPackageHeight()
    testBulkyPackageLength()
    testBulkyPackageAll()
    testNotBulkyPackage()
    testHeavyPackage()
    testNotHeavyPackage()
    testStandardPackage()
    testRejectedPackage()
    testSpecialPackageBulky()
    testSpecialPackageHeavy()

    print("all tests passed!")

if __name__ == "__main__":
    main()