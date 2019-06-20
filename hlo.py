
# import sys
# sys.setrecursionlimit(12000)

# print(sys.getrecursionlimit())

# g={0:[3,4,5], 1:[3,4,5], 2:[3,4,5], 3:[0,1,2], 4:[0,1,2], 5:[0,1,2]}
# l={0:[1,2], 1:[2,3], 2:[1,3], 3:[1,2], 4:[2,3], 5:[1,3]}


# g={0:[1,2,3], 1:[0,2,3], 2:[0,1,3], 3:[0,1,2]}
# l={0:[1,2,3], 1:[1,2,3], 2:[1,2,3], 3:[1,2,3], 4:[1,2,3], 5:[1,2,3], 6:[1,2,3], 7:[1,2,3], 8:[1,2,3], 9:[1,2,3]}
#
# g={0:[1,2,3],1:[0,4,5,6],2:[0,7,8],3:[0,9],4:[1,8,9],5:[1,7],6:[1,8],7:[2,5],8:[2,6],9:[3,4]}

# g={1:[2,3,4,5], 2:[1,4,6], 3:[1,4,6], 4:[1,2,3,6,5], 5:[1,6,4], 6:[2,3,4,5]}
# l={1:[1],2:[2,3],3:[3,4], 4:[3,4], 5:[3,4], 6:[2,3]}


# g={1:[4,5,6], 2:[4,5,6], 3:[4,5,6], 4:[1,2,3], 5:[1,2,3], 6:[1,2,3]}
# l={1:[1,2], 2:[2,3], 3:[1,3], 4:[1,2], 5:[2,3], 6:[1,3]}



# g={1:[2,5,6], 2:[1,3,7], 3:[2,4,8], 4:[3,5,9], 5:[1,4,10], 6:[1,8,9], 7:[2,9,10], 8:[3,10,6], 9:[4,6,7], 10:[5,7,8]}
# l={1:[1,2,3], 2:[2,3,4], 3:[1,2,3], 4:[1,2,4], 5:[2,3,4], 6:[1,2,3], 7:[1,2,3], 8:[1,2,3], 9:[1,2,3], 10:[1,2,3]}

# g={1:[3,4,5,6], 2:[3,4,5,6], 3:[1,2], 4:[1,2], 5:[1,2], 6:[1,2]}
# l={1:[1,2], 2:[3,4], 3:[1,3], 4:[1,4], 5:[2,3], 6:[2,4]}


# g={1: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 2: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 3: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 4: [1, 2, 3], 5: [1, 2, 3], 6: [1, 2, 3], 7: [1, 2, 3], 8: [1, 2, 3], 9: [1, 2, 3], 10:[1,2,3], 11: [1, 2, 3], 12: [1, 2, 3], 13: [1, 2, 3], 14: [1, 2, 3], 15: [1, 2, 3], 16: [1, 2, 3], 17: [1, 2, 3], 18: [1, 2, 3], 19: [1, 2, 3], 20: [1, 2, 3], 21: [1, 2, 3], 22: [1, 2, 3], 23: [1, 2, 3], 24: [1, 2, 3], 25: [1, 2, 3], 26: [1, 2, 3], 27: [1, 2, 3], 28: [1, 2, 3], 29: [1, 2, 3], 30:[1,2,3]}
# l={1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9], 4: [1, 4, 7], 5: [1, 4, 8], 6: [1, 4, 9], 7: [1, 5, 7], 8: [1, 5, 8], 9: [1, 5, 9], 10:[1,6,7], 11: [1, 6, 8], 12: [1, 6, 9], 13: [2, 4, 7], 14: [2, 4, 8], 15: [2, 4, 9], 16: [2, 5, 7], 17: [2, 5, 8], 18: [2, 5, 9], 19: [2, 6, 7], 20: [2, 6, 8], 21: [2, 6, 9], 22: [3, 4, 7], 23: [3, 4, 8], 24: [3, 4, 9], 25: [3, 5, 7], 26: [3, 5, 8], 27: [3, 5, 9], 28: [3, 6, 7], 29: [3, 6, 8], 30:[3,6,9]}








# g={1: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], 2: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], 3: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], 4: [1, 2, 3], 5: [1, 2, 3], 6: [1, 2, 3], 7: [1, 2, 3], 8: [1, 2, 3], 9: [1, 2, 3], 10:[1,2,3], 11: [1, 2, 3], 12: [1, 2, 3], 13: [1, 2, 3], 14: [1, 2, 3], 15: [1, 2, 3], 16: [1, 2, 3], 17: [1, 2, 3], 18: [1, 2, 3], 19: [1, 2, 3], 20: [1, 2, 3], 21: [1, 2, 3], 22: [1, 2, 3], 23: [1, 2, 3], 24: [1, 2, 3], 25: [1, 2, 3], 26: [1, 2, 3], 27: [1, 2, 3], 28: [1, 2, 3], 29: [1, 2, 3]}
# l={1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9], 4: [1, 4, 7], 5: [1, 4, 8], 6: [1, 4, 9], 7: [1, 5, 7], 8: [1, 5, 8], 9: [1, 5, 9], 10:[3,6,9], 11: [1, 6, 8], 12: [1, 6, 9], 13: [2, 4, 7], 14: [2, 4, 8], 15: [2, 4, 9], 16: [2, 5, 7], 17: [2, 5, 8], 18: [2, 5, 9], 19: [2, 6, 7], 20: [2, 6, 8], 21: [2, 6, 9], 22: [3, 4, 7], 23: [3, 4, 8], 24: [3, 4, 9], 25: [3, 5, 7], 26: [3, 5, 8], 27: [3, 5, 9], 28: [3, 6, 7], 29: [3, 6, 8]}


# g={1: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260], 2: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260], 3: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260], 4: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260], 5: [1, 2, 3, 4], 6: [1, 2, 3, 4], 7: [1, 2, 3, 4], 8: [1, 2, 3, 4], 9: [1, 2, 3, 4], 10: [1, 2, 3, 4], 11: [1, 2, 3, 4], 12: [1, 2, 3, 4], 13: [1, 2, 3, 4], 14: [1, 2, 3, 4], 15: [1, 2, 3, 4], 16: [1, 2, 3, 4], 17: [1, 2, 3, 4], 18: [1, 2, 3, 4], 19: [1, 2, 3, 4], 20: [1, 2, 3, 4], 21: [1, 2, 3, 4], 22: [1, 2, 3, 4], 23: [1, 2, 3, 4], 24: [1, 2, 3, 4], 25: [1, 2, 3, 4], 26: [1, 2, 3, 4], 27: [1, 2, 3, 4], 28: [1, 2, 3, 4], 29: [1, 2, 3, 4], 30: [1, 2, 3, 4], 31: [1, 2, 3, 4], 32: [1, 2, 3, 4], 33: [1, 2, 3, 4], 34: [1, 2, 3, 4], 35: [1, 2, 3, 4], 36: [1, 2, 3, 4], 37: [1, 2, 3, 4], 38: [1, 2, 3, 4], 39: [1, 2, 3, 4], 40: [1, 2, 3, 4], 41: [1, 2, 3, 4], 42: [1, 2, 3, 4], 43: [1, 2, 3, 4], 44: [1, 2, 3, 4], 45: [1, 2, 3, 4], 46: [1, 2, 3, 4], 47: [1, 2, 3, 4], 48: [1, 2, 3, 4], 49: [1, 2, 3, 4], 50: [1, 2, 3, 4], 51: [1, 2, 3, 4], 52: [1, 2, 3, 4], 53: [1, 2, 3, 4], 54: [1, 2, 3, 4], 55: [1, 2, 3, 4], 56: [1, 2, 3, 4], 57: [1, 2, 3, 4], 58: [1, 2, 3, 4], 59: [1, 2, 3, 4], 60: [1, 2, 3, 4], 61: [1, 2, 3, 4], 62: [1, 2, 3, 4], 63: [1, 2, 3, 4], 64: [1, 2, 3, 4], 65: [1, 2, 3, 4], 66: [1, 2, 3, 4], 67: [1, 2, 3, 4], 68: [1, 2, 3, 4], 69: [1, 2, 3, 4], 70: [1, 2, 3, 4], 71: [1, 2, 3, 4], 72: [1, 2, 3, 4], 73: [1, 2, 3, 4], 74: [1, 2, 3, 4], 75: [1, 2, 3, 4], 76: [1, 2, 3, 4], 77: [1, 2, 3, 4], 78: [1, 2, 3, 4], 79: [1, 2, 3, 4], 80: [1, 2, 3, 4], 81: [1, 2, 3, 4], 82: [1, 2, 3, 4], 83: [1, 2, 3, 4], 84: [1, 2, 3, 4], 85: [1, 2, 3, 4], 86: [1, 2, 3, 4], 87: [1, 2, 3, 4], 88: [1, 2, 3, 4], 89: [1, 2, 3, 4], 90: [1, 2, 3, 4], 91: [1, 2, 3, 4], 92: [1, 2, 3, 4], 93: [1, 2, 3, 4], 94: [1, 2, 3, 4], 95: [1, 2, 3, 4], 96: [1, 2, 3, 4], 97: [1, 2, 3, 4], 98: [1, 2, 3, 4], 99: [1, 2, 3, 4], 100: [1, 2, 3, 4], 101: [1, 2, 3, 4], 102: [1, 2, 3, 4], 103: [1, 2, 3, 4], 104: [1, 2, 3, 4], 105: [1, 2, 3, 4], 106: [1, 2, 3, 4], 107: [1, 2, 3, 4], 108: [1, 2, 3, 4], 109: [1, 2, 3, 4], 110: [1, 2, 3, 4], 111: [1, 2, 3, 4], 112: [1, 2, 3, 4], 113: [1, 2, 3, 4], 114: [1, 2, 3, 4], 115: [1, 2, 3, 4], 116: [1, 2, 3, 4], 117: [1, 2, 3, 4], 118: [1, 2, 3, 4], 119: [1, 2, 3, 4], 120: [1, 2, 3, 4], 121: [1, 2, 3, 4], 122: [1, 2, 3, 4], 123: [1, 2, 3, 4], 124: [1, 2, 3, 4], 125: [1, 2, 3, 4], 126: [1, 2, 3, 4], 127: [1, 2, 3, 4], 128: [1, 2, 3, 4], 129: [1, 2, 3, 4], 130: [1, 2, 3, 4], 131: [1, 2, 3, 4], 132: [1, 2, 3, 4], 133: [1, 2, 3, 4], 134: [1, 2, 3, 4], 135: [1, 2, 3, 4], 136: [1, 2, 3, 4], 137: [1, 2, 3, 4], 138: [1, 2, 3, 4], 139: [1, 2, 3, 4], 140: [1, 2, 3, 4], 141: [1, 2, 3, 4], 142: [1, 2, 3, 4], 143: [1, 2, 3, 4], 144: [1, 2, 3, 4], 145: [1, 2, 3, 4], 146: [1, 2, 3, 4], 147: [1, 2, 3, 4], 148: [1, 2, 3, 4], 149: [1, 2, 3, 4], 150: [1, 2, 3, 4], 151: [1, 2, 3, 4], 152: [1, 2, 3, 4], 153: [1, 2, 3, 4], 154: [1, 2, 3, 4], 155: [1, 2, 3, 4], 156: [1, 2, 3, 4], 157: [1, 2, 3, 4], 158: [1, 2, 3, 4], 159: [1, 2, 3, 4], 160: [1, 2, 3, 4], 161: [1, 2, 3, 4], 162: [1, 2, 3, 4], 163: [1, 2, 3, 4], 164: [1, 2, 3, 4], 165: [1, 2, 3, 4], 166: [1, 2, 3, 4], 167: [1, 2, 3, 4], 168: [1, 2, 3, 4], 169: [1, 2, 3, 4], 170: [1, 2, 3, 4], 171: [1, 2, 3, 4], 172: [1, 2, 3, 4], 173: [1, 2, 3, 4], 174: [1, 2, 3, 4], 175: [1, 2, 3, 4], 176: [1, 2, 3, 4], 177: [1, 2, 3, 4], 178: [1, 2, 3, 4], 179: [1, 2, 3, 4], 180: [1, 2, 3, 4], 181: [1, 2, 3, 4], 182: [1, 2, 3, 4], 183: [1, 2, 3, 4], 184: [1, 2, 3, 4], 185: [1, 2, 3, 4], 186: [1, 2, 3, 4], 187: [1, 2, 3, 4], 188: [1, 2, 3, 4], 189: [1, 2, 3, 4], 190: [1, 2, 3, 4], 191: [1, 2, 3, 4], 192: [1, 2, 3, 4], 193: [1, 2, 3, 4], 194: [1, 2, 3, 4], 195: [1, 2, 3, 4], 196: [1, 2, 3, 4], 197: [1, 2, 3, 4], 198: [1, 2, 3, 4], 199: [1, 2, 3, 4], 200: [1, 2, 3, 4], 201: [1, 2, 3, 4], 202: [1, 2, 3, 4], 203: [1, 2, 3, 4], 204: [1, 2, 3, 4], 205: [1, 2, 3, 4], 206: [1, 2, 3, 4], 207: [1, 2, 3, 4], 208: [1, 2, 3, 4], 209: [1, 2, 3, 4], 210: [1, 2, 3, 4], 211: [1, 2, 3, 4], 212: [1, 2, 3, 4], 213: [1, 2, 3, 4], 214: [1, 2, 3, 4], 215: [1, 2, 3, 4], 216: [1, 2, 3, 4], 217: [1, 2, 3, 4], 218: [1, 2, 3, 4], 219: [1, 2, 3, 4], 220: [1, 2, 3, 4], 221: [1, 2, 3, 4], 222: [1, 2, 3, 4], 223: [1, 2, 3, 4], 224: [1, 2, 3, 4], 225: [1, 2, 3, 4], 226: [1, 2, 3, 4], 227: [1, 2, 3, 4], 228: [1, 2, 3, 4], 229: [1, 2, 3, 4], 230: [1, 2, 3, 4], 231: [1, 2, 3, 4], 232: [1, 2, 3, 4], 233: [1, 2, 3, 4], 234: [1, 2, 3, 4], 235: [1, 2, 3, 4], 236: [1, 2, 3, 4], 237: [1, 2, 3, 4], 238: [1, 2, 3, 4], 239: [1, 2, 3, 4], 240: [1, 2, 3, 4], 241: [1, 2, 3, 4], 242: [1, 2, 3, 4], 243: [1, 2, 3, 4], 244: [1, 2, 3, 4], 245: [1, 2, 3, 4], 246: [1, 2, 3, 4], 247: [1, 2, 3, 4], 248: [1, 2, 3, 4], 249: [1, 2, 3, 4], 250: [1, 2, 3, 4], 251: [1, 2, 3, 4], 252: [1, 2, 3, 4], 253: [1, 2, 3, 4], 254: [1, 2, 3, 4], 255: [1, 2, 3, 4], 256: [1, 2, 3, 4], 257: [1, 2, 3, 4], 258: [1, 2, 3, 4], 259: [1, 2, 3, 4], 260: [1, 2, 3, 4]}
#
# l={1: [1, 2, 3, 4], 2: [5, 6, 7, 8], 3: [9, 10, 11, 12], 4: [13, 14, 15, 16], 5: [1, 5, 9, 13], 6: [1, 5, 9, 14], 7: [1, 5, 9, 15], 8: [1, 5, 9, 16], 9: [1, 5, 10, 13], 10: [1, 5, 10, 14], 11: [1, 5, 10, 15], 12: [1, 5, 10, 16], 13: [1, 5, 11, 13], 14: [1, 5, 11, 14], 15: [1, 5, 11, 15], 16: [1, 5, 11, 16], 17: [1, 5, 12, 13], 18: [1, 5, 12, 14], 19: [1, 5, 12, 15], 20: [1, 5, 12, 16], 21: [1, 6, 9, 13], 22: [1, 6, 9, 14], 23: [1, 6, 9, 15], 24: [1, 6, 9, 16], 25: [1, 6, 10, 13], 26: [1, 6, 10, 14], 27: [1, 6, 10, 15], 28: [1, 6, 10, 16], 29: [1, 6, 11, 13], 30: [1, 6, 11, 14], 31: [1, 6, 11, 15], 32: [1, 6, 11, 16], 33: [1, 6, 12, 13], 34: [1, 6, 12, 14], 35: [1, 6, 12, 15], 36: [1, 6, 12, 16], 37: [1, 7, 9, 13], 38: [1, 7, 9, 14], 39: [1, 7, 9, 15], 40: [1, 7, 9, 16], 41: [1, 7, 10, 13], 42: [1, 7, 10, 14], 43: [1, 7, 10, 15], 44: [1, 7, 10, 16], 45: [1, 7, 11, 13], 46: [1, 7, 11, 14], 47: [1, 7, 11, 15], 48: [1, 7, 11, 16], 49: [1, 7, 12, 13], 50: [1, 7, 12, 14], 51: [1, 7, 12, 15], 52: [1, 7, 12, 16], 53: [1, 8, 9, 13], 54: [1, 8, 9, 14], 55: [1, 8, 9, 15], 56: [1, 8, 9, 16], 57: [1, 8, 10, 13], 58: [1, 8, 10, 14], 59: [1, 8, 10, 15], 60: [1, 8, 10, 16], 61: [1, 8, 11, 13], 62: [1, 8, 11, 14], 63: [1, 8, 11, 15], 64: [1, 8, 11, 16], 65: [1, 8, 12, 13], 66: [1, 8, 12, 14], 67: [1, 8, 12, 15], 68: [1, 8, 12, 16], 69: [2, 5, 9, 13], 70: [2, 5, 9, 14], 71: [2, 5, 9, 15], 72: [2, 5, 9, 16], 73: [2, 5, 10, 13], 74: [2, 5, 10, 14], 75: [2, 5, 10, 15], 76: [2, 5, 10, 16], 77: [2, 5, 11, 13], 78: [2, 5, 11, 14], 79: [2, 5, 11, 15], 80: [2, 5, 11, 16], 81: [2, 5, 12, 13], 82: [2, 5, 12, 14], 83: [2, 5, 12, 15], 84: [2, 5, 12, 16], 85: [2, 6, 9, 13], 86: [2, 6, 9, 14], 87: [2, 6, 9, 15], 88: [2, 6, 9, 16], 89: [2, 6, 10, 13], 90: [2, 6, 10, 14], 91: [2, 6, 10, 15], 92: [2, 6, 10, 16], 93: [2, 6, 11, 13], 94: [2, 6, 11, 14], 95: [2, 6, 11, 15], 96: [2, 6, 11, 16], 97: [2, 6, 12, 13], 98: [2, 6, 12, 14], 99: [2, 6, 12, 15], 100: [2, 6, 12, 16], 101: [2, 7, 9, 13], 102: [2, 7, 9, 14], 103: [2, 7, 9, 15], 104: [2, 7, 9, 16], 105: [2, 7, 10, 13], 106: [2, 7, 10, 14], 107: [2, 7, 10, 15], 108: [2, 7, 10, 16], 109: [2, 7, 11, 13], 110: [2, 7, 11, 14], 111: [2, 7, 11, 15], 112: [2, 7, 11, 16], 113: [2, 7, 12, 13], 114: [2, 7, 12, 14], 115: [2, 7, 12, 15], 116: [2, 7, 12, 16], 117: [2, 8, 9, 13], 118: [2, 8, 9, 14], 119: [2, 8, 9, 15], 120: [2, 8, 9, 16], 121: [2, 8, 10, 13], 122: [2, 8, 10, 14], 123: [2, 8, 10, 15], 124: [2, 8, 10, 16], 125: [2, 8, 11, 13], 126: [2, 8, 11, 14], 127: [2, 8, 11, 15], 128: [2, 8, 11, 16], 129: [2, 8, 12, 13], 130: [2, 8, 12, 14], 131: [2, 8, 12, 15], 132: [2, 8, 12, 16], 133: [3, 5, 9, 13], 134: [3, 5, 9, 14], 135: [3, 5, 9, 15], 136: [3, 5, 9, 16], 137: [3, 5, 10, 13], 138: [3, 5, 10, 14], 139: [3, 5, 10, 15], 140: [3, 5, 10, 16], 141: [3, 5, 11, 13], 142: [3, 5, 11, 14], 143: [3, 5, 11, 15], 144: [3, 5, 11, 16], 145: [3, 5, 12, 13], 146: [3, 5, 12, 14], 147: [3, 5, 12, 15], 148: [3, 5, 12, 16], 149: [3, 6, 9, 13], 150: [3, 6, 9, 14], 151: [3, 6, 9, 15], 152: [3, 6, 9, 16], 153: [3, 6, 10, 13], 154: [3, 6, 10, 14], 155: [3, 6, 10, 15], 156: [3, 6, 10, 16], 157: [3, 6, 11, 13], 158: [3, 6, 11, 14], 159: [3, 6, 11, 15], 160: [3, 6, 11, 16], 161: [3, 6, 12, 13], 162: [3, 6, 12, 14], 163: [3, 6, 12, 15], 164: [3, 6, 12, 16], 165: [3, 7, 9, 13], 166: [3, 7, 9, 14], 167: [3, 7, 9, 15], 168: [3, 7, 9, 16], 169: [3, 7, 10, 13], 170: [3, 7, 10, 14], 171: [3, 7, 10, 15], 172: [3, 7, 10, 16], 173: [3, 7, 11, 13], 174: [3, 7, 11, 14], 175: [3, 7, 11, 15], 176: [3, 7, 11, 16], 177: [3, 7, 12, 13], 178: [3, 7, 12, 14], 179: [3, 7, 12, 15], 180: [3, 7, 12, 16], 181: [3, 8, 9, 13], 182: [3, 8, 9, 14], 183: [3, 8, 9, 15], 184: [3, 8, 9, 16], 185: [3, 8, 10, 13], 186: [3, 8, 10, 14], 187: [3, 8, 10, 15], 188: [3, 8, 10, 16], 189: [3, 8, 11, 13], 190: [3, 8, 11, 14], 191: [3, 8, 11, 15], 192: [3, 8, 11, 16], 193: [3, 8, 12, 13], 194: [3, 8, 12, 14], 195: [3, 8, 12, 15], 196: [3, 8, 12, 16], 197: [4, 5, 9, 13], 198: [4, 5, 9, 14], 199: [4, 5, 9, 15], 200: [4, 5, 9, 16], 201: [4, 5, 10, 13], 202: [4, 5, 10, 14], 203: [4, 5, 10, 15], 204: [4, 5, 10, 16], 205: [4, 5, 11, 13], 206: [4, 5, 11, 14], 207: [4, 5, 11, 15], 208: [4, 5, 11, 16], 209: [4, 5, 12, 13], 210: [4, 5, 12, 14], 211: [4, 5, 12, 15], 212: [4, 5, 12, 16], 213: [4, 6, 9, 13], 214: [4, 6, 9, 14], 215: [4, 6, 9, 15], 216: [4, 6, 9, 16], 217: [4, 6, 10, 13], 218: [4, 6, 10, 14], 219: [4, 6, 10, 15], 220: [4, 6, 10, 16], 221: [4, 6, 11, 13], 222: [4, 6, 11, 14], 223: [4, 6, 11, 15], 224: [4, 6, 11, 16], 225: [4, 6, 12, 13], 226: [4, 6, 12, 14], 227: [4, 6, 12, 15], 228: [4, 6, 12, 16], 229: [4, 7, 9, 13], 230: [4, 7, 9, 14], 231: [4, 7, 9, 15], 232: [4, 7, 9, 16], 233: [4, 7, 10, 13], 234: [4, 7, 10, 14], 235: [4, 7, 10, 15], 236: [4, 7, 10, 16], 237: [4, 7, 11, 13], 238: [4, 7, 11, 14], 239: [4, 7, 11, 15], 240: [4, 7, 11, 16], 241: [4, 7, 12, 13], 242: [4, 7, 12, 14], 243: [4, 7, 12, 15], 244: [4, 7, 12, 16], 245: [4, 8, 9, 13], 246: [4, 8, 9, 14], 247: [4, 8, 9, 15], 248: [4, 8, 9, 16], 249: [4, 8, 10, 13], 250: [4, 8, 10, 14], 251: [4, 8, 10, 15], 252: [4, 8, 10, 16], 253: [4, 8, 11, 13], 254: [4, 8, 11, 14], 255: [4, 8, 11, 15], 256: [4, 8, 11, 16], 257: [4, 8, 12, 13], 258: [4, 8, 12, 14], 259: [4, 8, 12, 15], 260: [4, 8, 12, 16]}



# g={1: [2, 4, 10, 11, 13, 16, 17], 2: [1, 3, 5, 12, 13, 14, 17], 3: [2, 4, 6, 7, 13, 14, 15], 4: [1, 3, 8, 9, 13, 15, 16], 5: [2, 6, 14], 6: [3, 5, 14], 7: [3, 8, 15], 8: [4, 7, 15], 9: [4, 10, 16], 10: [1, 9, 16], 11: [1, 12, 17], 12: [2, 11, 17], 13: [1, 2, 3, 4], 14: [2, 3, 5, 6], 15: [3, 4, 7, 8], 16: [1, 4, 9, 10], 17: [1, 2, 11, 12]}





# g={1: [2, 4, 10, 11, 13, 16, 17, 18], 2: [1, 3, 5, 12, 13, 14, 17, 18], 3: [2, 4, 6, 7, 13, 14, 15, 18], 4: [1, 3, 8, 9, 13, 15, 16, 18], 5: [2, 6, 14, 18], 6: [3, 5, 14, 18], 7: [3, 8, 15, 18], 8: [4, 7, 15, 18], 9: [4, 10, 16, 18], 10: [1, 9, 16, 18], 11: [1, 12, 17, 18], 12: [2, 11, 17, 18], 13: [1, 2, 3, 4], 14: [2, 3, 5, 6], 15: [3, 4, 7, 8], 16: [1, 4, 9, 10], 17: [1, 2, 11, 12], 18: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}
# l={1: [5, 2, 3, 4], 2: [5, 1, 3, 4], 3: [5, 1, 2, 4], 4: [5, 1, 2, 3], 5: [5, 1, 2, 3], 6: [5, 2, 3, 4], 7: [5, 2, 3, 4], 8: [5, 1, 3, 4], 9: [5, 1, 3, 4], 10: [5, 1, 2, 4], 11: [5, 1, 2, 4], 12: [5, 1, 2, 3], 13: [1, 2, 3, 4], 14: [1, 2, 3, 4], 15: [1, 2, 3, 4], 16: [1, 2, 3, 4], 17: [1, 2, 3, 4], 18:[5]}






g={1: [2, 4, 10, 11, 13, 16, 17, 69], 2: [1, 3, 5, 12, 13, 14, 17, 69], 3: [2, 4, 6, 7, 13, 14, 15, 69], 4: [1, 3, 8, 9, 13, 15, 16, 69], 5: [2, 6, 14, 69], 6: [3, 5, 14, 69], 7: [3, 8, 15, 69], 8: [4, 7, 15, 69], 9: [4, 10, 16, 69], 10: [1, 9, 16, 69], 11: [1, 12, 17, 69], 12: [2, 11, 17, 69], 13: [1, 2, 3, 4], 14: [2, 3, 5, 6], 15: [3, 4, 7, 8], 16: [1, 4, 9, 10], 17: [1, 2, 11, 12], 18: [19, 21, 27, 28, 30, 33, 34, 69], 19: [18, 20, 22, 29, 30, 31, 34, 69], 20: [19, 21, 23, 24, 30, 31, 32, 69], 21: [18, 20, 25, 26, 30, 32, 33, 69], 22: [19, 23, 31, 69], 23: [20, 22, 31, 69], 24: [20, 25, 32, 69], 25: [21, 24, 32, 69], 26: [21, 27, 33, 69], 27: [18, 26, 33, 69], 28: [18, 29, 34, 69], 29: [19, 28, 34, 69], 30: [18, 19, 20, 21], 31: [19, 20, 22, 23], 32: [20, 21, 24, 25], 33: [18, 21, 26, 27], 34: [18, 19, 28, 29], 35: [36, 38, 44, 45, 47, 50, 51, 69], 36: [35, 37, 39, 46, 47, 48, 51, 69], 37: [36, 38, 40, 41, 47, 48, 49, 69], 38: [35, 37, 42, 43, 47, 49, 50, 69], 39: [36, 40, 48, 69], 40: [37, 39, 48, 69], 41: [37, 42, 49, 69], 42: [38, 41, 49, 69], 43: [38, 44, 50, 69], 44: [35, 43, 50, 69], 45: [35, 46, 51, 69], 46: [36, 45, 51, 69], 47: [35, 36, 37, 38], 48: [36, 37, 39, 40], 49: [37, 38, 41, 42], 50: [35, 38, 43, 44], 51: [35, 36, 45, 46], 52: [53, 55, 61, 62, 64, 67, 68, 69], 53: [52, 54, 56, 63, 64, 65, 68, 69], 54: [53, 55, 57, 58, 64, 65, 66, 69], 55: [52, 54, 59, 60, 64, 66, 67, 69], 56: [53, 57, 65, 69], 57: [54, 56, 65, 69], 58: [54, 59, 66, 69], 59: [55, 58, 66, 69], 60: [55, 61, 67, 69], 61: [52, 60, 67, 69], 62: [52, 63, 68, 69], 63: [53, 62, 68, 69], 64: [52, 53, 54, 55], 65: [53, 54, 56, 57], 66: [54, 55, 58, 59], 67: [52, 55, 60, 61], 68: [52, 53, 62, 63], 69: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]}
l={1: [5, 2, 3, 4], 2: [5, 1, 3, 4], 3: [5, 1, 2, 4], 4: [5, 1, 2, 3], 5: [5, 1, 2, 3], 6: [5, 2, 3, 4], 7: [5, 2, 3, 4], 8: [5, 1, 3, 4], 9: [5, 1, 3, 4], 10: [5, 1, 2, 4], 11: [5, 1, 2, 4], 12: [5, 1, 2, 3], 13: [1, 2, 3, 4], 14: [1, 2, 3, 4], 15: [1, 2, 3, 4], 16: [1, 2, 3, 4], 17: [1, 2, 3, 4], 18: [2, 3, 4, 6], 19: [1, 3, 4, 6], 20: [1, 2, 4, 6], 21: [1, 2, 3, 6], 22: [1, 2, 3, 6], 23: [2, 3, 4, 6], 24: [2, 3, 4, 6], 25: [1, 3, 4, 6], 26: [1, 3, 4, 6], 27: [1, 2, 4, 6], 28: [1, 2, 4, 6], 29: [1, 2, 3, 6], 30: [1, 2, 3, 4], 31: [1, 2, 3, 4], 32: [1, 2, 3, 4], 33: [1, 2, 3, 4], 34: [1, 2, 3, 4], 35: [2, 3, 4, 7], 36: [1, 3, 4, 7], 37: [1, 2, 4, 7], 38: [1, 2, 3, 7], 39: [1, 2, 3, 7], 40: [2, 3, 4, 7], 41: [2, 3, 4, 7], 42: [1, 3, 4, 7], 43: [1, 3, 4, 7], 44: [1, 2, 4, 7], 45: [1, 2, 4, 7], 46: [1, 2, 3, 7], 47: [1, 2, 3, 4], 48: [1, 2, 3, 4], 49: [1, 2, 3, 4], 50: [1, 2, 3, 4], 51: [1, 2, 3, 4], 52: [2, 3, 4, 8], 53: [1, 3, 4, 8], 54: [1, 2, 4, 8], 55: [1, 2, 3, 8], 56: [1, 2, 3, 8], 57: [2, 3, 4, 8], 58: [2, 3, 4, 8], 59: [1, 3, 4, 8], 60: [1, 3, 4, 8], 61: [1, 2, 4, 8], 62: [1, 2, 4, 8], 63: [1, 2, 3, 8], 64: [1, 2, 3, 4], 65: [1, 2, 3, 4], 66: [1, 2, 3, 4], 67: [1, 2, 3, 4], 68: [1, 2, 3, 4], 69: [5, 6, 7, 8]}



# Graph(g).show(layout="planar")
#Bredth First Search
visiting=[1]
visited=[]
parent={1:-1}
distance={1:0}
dist=0
tree={}

nov= 69

while visiting:
    x=visiting.pop(0)

    if(not visiting or parent[x] is not parent[visited[-1]]):
        dist+=1
    visited.append(x)
    for v in g[x]:
        if v not in visited  and v not in visiting:
            visiting.append(v)
            parent[v]=x
            distance[v]=dist
            if x in tree:
                tree[x].append(v)
            else:
                tree[x]=[v]

# print("The breadth first search tree is : ", end="")
print(parent)
print(distance)
print(visited)
print(tree)

# Graph(tree).show(layout="tree")


def is_valid(g,v,col,c):
    for n in g[v]:
        if c[n] == col:
            return False
    return True




c = {x: 0 for x in range(1,nov+1)}
checked = {x: [] for x in range(1,nov+1)}
ind=0
# while ind < 4:
#     key = 0
#     for col in l[visited[ind]]:
#         if (is_valid(g, visited[ind], col, c)) and (col not in checked[visited[ind]]):
#             c[visited[ind]] = col
#             checked[visited[ind]].append(col)
#             key = 1
#             break
#
#     if (key == 0):
#         #         print("hahahahaha")
#         if (ind == 0):
#             sp = 1
#             print("The graph 'g' is not colorable by the list 'l'")
#             break
#
#         dad = parent[visited[ind]]
#         dad_ind = visited.index(dad)
#         for n in range(dad_ind, ind):
#             c[visited[n]] = 0
#             checked[visited[n + 1]] = []
#         ind = dad_ind
#     else:
#         ind += 1
#
# print(c)
# print(checked)

def is_colorable(ind,visited,c,checked,parent):
    if(ind == nov):
        print(c)
        return 1
    key = 0
    for col in l[visited[ind]]:
        if (is_valid(g, visited[ind], col, c)) and (col not in checked[visited[ind]]):
            c[visited[ind]] = col
            checked[visited[ind]].append(col)
            key = 1
            break

    if (key == 0):
        if (ind == 0):
             return 0

        dad = parent[visited[ind]]
        dad_ind = visited.index(dad)


        clashed_colors =[]
        clashed_indices =[]

        for n in range(dad_ind, ind):
            if(c[visited[n]] in l[visited[ind]]) and (c[visited[n]] not in clashed_colors):
                clashed_colors.append(c[visited[n]])
                clashed_indices.append(n)




        # clashed_indices.reverse()

        c_ = dict(c)
        checked_ = dict(checked)



        for m in (clashed_indices) :
            for n in range(m,ind):
                c[visited[n]] = 0
                checked[visited[n + 1]] = []


            if(is_colorable(m,visited,c,checked,parent) == 1):
               return 1
            else:
                c = dict(c_)
                checked = dict(checked_)

        return 0




    else:
        return is_colorable(ind + 1, visited, c, checked, parent)










print()
print()

if(is_colorable(0,visited,c,checked,parent)==0):
    print("not colorable")



# chromaticity=2
# while True:
#     l={y:list(range(1,chromaticity+1)) for y in range (1,nov+1)}
#     if (is_colorable(0, visited, c, checked, parent) == 1):
#         print(chromaticity)
#         print(l)
#         break
#     chromaticity+=1

