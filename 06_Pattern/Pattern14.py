# Marging patterns
# decermental
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

for i in range(1, 6):
    for j in range(1, i):
        print(' ', end=" ")  # print space
    for j in range(1, 7 - i):
        print('*', end=" ")  # print star
    print()
