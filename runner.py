from Finch import Errors, Finch

robot = Finch("Hampton",1)

tests = {

    "A": robot.beakLight(20, 20, 20),
    "B": robot.setMove("F", 20, 100),
    "C": robot.setTurn("R", 20, 100),
    "D": robot.setMotors(100, 0),
    "E": robot.setTail(3,100,50,20),
    "F": robot.playNote(60, 1),
    "G": robot.setDisplay([1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1]),
    "H": robot.setPoint(3,3,1),
    "I": robot.digiPrint("TEST")
}


for test in tests:
    print(test)

print("all tests passed")
