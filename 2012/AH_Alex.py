import sys

# Read input parameters
str_input = sys.stdin.readline().strip().split(',')
rows = int(str_input[0])
columns = int(str_input[1])

robot1_init_col = int(sys.stdin.readline().strip())
robot2_init_col = int(sys.stdin.readline().strip())
init_ball_holder = int(sys.stdin.readline().strip())
num_obstacles = int(sys.stdin.readline().strip())

obstacles = []
for i in range(0, num_obstacles):
    str_input = sys.stdin.readline().strip().split(',')
    obstacles.append([int(str_input[0]), int(str_input[1])])

#print "Obstacles:"
#print obstacles

move_sequence = sys.stdin.readline().strip()
used_move_sequence = ""

move_seq_index = 0

robot_pos = []
robot_pos.append([0, robot1_init_col])
robot_pos.append([rows - 1, robot2_init_col])
#print 'Init Ball Holder: ' + str(init_ball_holder)
ball_pos = [robot_pos[init_ball_holder - 1][0], robot_pos[init_ball_holder - 1][1]]
#print 'Init Ball Pos: [%s, %s]' % (ball_pos[0], ball_pos[1])
ball_vel = [0, 0]

# raise Exception(str(rows) + "x" + str(columns) + "\n" + str(ball_pos) + "\n" + str(robot_pos[0]) + "\n" + str(robot_pos[1]) + "\n" + str(move_sequence) + "\n" + str(obstacles))

def throw_ball(robot_index, move_sequence, move_sequence_index, move_string):
    ball_vel = []
    #print 'Robot %s throwing ball in direction %s.' % (robot_index, move_sequence[move_sequence_index])
    if robot_index == 0:
        if move_sequence[move_sequence_index] == 'S':
            ball_vel = [1, 0]
        elif move_sequence[move_sequence_index] == 'R':
            ball_vel = [1, 1]
        elif move_sequence[move_sequence_index] == 'L':
            ball_vel = [1, -1]
    elif robot_index == 1:
        if move_sequence[move_sequence_index] == 'S':
            ball_vel = [-1, 0]
        elif move_sequence[move_sequence_index] == 'R':
            ball_vel = [-1, 1]
        elif move_sequence[move_sequence_index] == 'L':
            ball_vel = [-1, -1]

    return (ball_vel, move_sequence_index + 1, move_string + move_sequence[move_sequence_index])

def obstacle_bounce(ball_vel):
    #print 'Ball hits obstacle.'
    if ball_vel == [-1, 0]:
        return [1, 0]
    elif ball_vel == [-1, 1]:
        return [-1, -1]
    elif ball_vel == [-1, -1]:
        return [-1, 1]
    if ball_vel == [1, 0]:
        return [-1, 0]
    elif ball_vel == [1, 1]:
        return [1, -1]
    elif ball_vel == [1, -1]:
        return [1, 1]

    raise Exception("Ball had invalid velocity.")

def wall_bounce(ball_vel):
    #print 'Ball hits wall.'
    if ball_vel == [-1, 1]:
        return [-1, -1]
    elif ball_vel == [-1, -1]:
        return [-1, 1]
    elif ball_vel == [1, 1]:
        return [1, -1]
    elif ball_vel == [1, -1]:
        return [1, 1]
    else:
        return ball_vel

def move_robot(robot_pos, ball_pos, columns):
    #print 'Moving robot from Pos: [%s, %s] B:[%s, %s]' % (robot_pos[0], robot_pos[1], ball_pos[0], ball_pos[1])
    if robot_pos[1] == ball_pos[1]: # Robot is on the same column as the ball
        if robot_pos[1] + 1 < columns:
            return [robot_pos[0], robot_pos[1] + 1]
        else:
            return [robot_pos[0], robot_pos[1] - 1]

    if robot_pos[1] < ball_pos[1]: # Robot is on the left of the ball
        if robot_pos[1] + 1 >= columns:
            return [robot_pos[0], robot_pos[1] - 1]
        else:
            return [robot_pos[0], robot_pos[1] + 1]

    if robot_pos[1] > ball_pos[1]: # Robot is on the right of the ball
        if robot_pos[1] - 1 < 0:
            return [robot_pos[0], robot_pos[1] + 1]
        else:
            return [robot_pos[0], robot_pos[1] - 1]

# Run the simulation
game_over = False
winner = -1 # -1 for tie, 0 for robot 1, 1 for robot 2
first_pass = True
while not game_over:
    # Update the ball's position
    #print 'Start Vel: [%s, %s]' % (ball_vel[0], ball_vel[1])
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    #print 'Ball Pos: [%s, %s]' % (ball_pos[0], ball_pos[1])

    next_ball_pos = [ball_pos[0] + ball_vel[0], ball_pos[1] + ball_vel[1]]

    if not first_pass:
        # Update the position of the robots
        robot_pos[0] = move_robot(robot_pos[0], ball_pos, columns)
        #print 'Moved robot to Pos: [%s, %s]' % (robot_pos[0][0], robot_pos[0][1])
        robot_pos[1] = move_robot(robot_pos[1], ball_pos, columns)
        #print 'Moved robot to Pos: [%s, %s]' % (robot_pos[1][0], robot_pos[1][1])

    # Update the ball's velocity

    # Check if the ball is currently at a robot's position, and have the robot
    # throw the ball accordingly (or end the game)
    if ball_pos == robot_pos[0]:
        if move_seq_index >= len(move_sequence):
            game_over = True
            break
        else:
            ball_vel, move_seq_index, used_move_sequence =  throw_ball(0, move_sequence, move_seq_index, used_move_sequence)
    elif ball_pos == robot_pos[1]:
        if move_seq_index >= len(move_sequence):
            game_over = True
            break
        else:
            ball_vel, move_seq_index, used_move_sequence =  throw_ball(1, move_sequence, move_seq_index, used_move_sequence)

    # Check if the ball is colliding with an obstacle, and adjust its velocity accordingly
    if ball_pos in obstacles:
        ball_vel = obstacle_bounce(ball_vel)

    # Check if the ball is colliding with a wall, and adjust its velocity accordingly
    if (ball_pos[1] == 0 and ball_vel[1] == -1) or (ball_pos[1] == columns - 1 and ball_vel[1] == 1):
        ball_vel = wall_bounce(ball_vel)

    #print 'End Vel: [%s, %s]' % (ball_vel[0], ball_vel[1])

    if(ball_pos[0] == 0 and ball_pos != robot_pos[0]):
        game_over = True
        winner = 1
        #break

    if(ball_pos[0] == rows - 1 and ball_pos != robot_pos[1]):
        game_over = True
        winner = 0
        #break

    first_pass = False

    #print 'Robot1 Pos: [%s, %s]' % (robot_pos[0][0], robot_pos[0][1])
    #print 'Robot2 Pos: [%s, %s]' % (robot_pos[1][0], robot_pos[1][1])
    #print ''

# Print the winner
if winner == -1:
    print "This game does not have a Winner."
elif winner == 0:
    print "Winner: Robot1"
elif winner == 1:
    print "Winner: Robot2"

# Print the robot positions
print "Robot1 At [%s,%s]" % (robot_pos[0][0], robot_pos[0][1])
print "Robot2 At [%s,%s]" % (robot_pos[1][0], robot_pos[1][1])

# Print the ball positions
print "Ball At [%s,%s]" % (ball_pos[0], ball_pos[1])

# Print the move sequence
print "Sequence: " + used_move_sequence