from utils import color, gclassroom, logger

Classroom = gclassroom.Classroom() 
ClassroomHelper = gclassroom.ClassroomHelper(classroom=Classroom) 
Color = color.Color()
Logger = logger.Logger()

def help():
    Logger.notice("classroom-cli v0.0.1:")
    print("h | Displays this menu\nlc | Lists courses that you are enrolled in\nla | Lists assignments that are due to be turned in\nstop | Closes the application")

def menu():
    Logger.info("Type a command or use 'h' or 'help' for help")
    parseCommand(input(Color.BLUE + "> " + Color.END))

def parseCommand(command):
    if command in ("h", "help"):
        help()
    elif command in ("lc", "listcourses"):
        ClassroomHelper.listCourses()
    elif command in ("la", "listassignments"):
        ClassroomHelper.listAssignmentsBatch()
    elif command in ("x", "exit", "stop"):
        exit(0)
    else:
        Logger.error("Unknown command!")
        
    menu()

if __name__ == '__main__':
    Classroom.initialize()

    # pylint: disable=no-member
    student = Classroom.service.userProfiles().get(userId="me").execute()
    name = student.get("name").get("fullName")

    Logger.success(Color.BOLD + "You are logged in as " + name)

    menu()