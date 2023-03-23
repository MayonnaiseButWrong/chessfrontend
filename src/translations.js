let toXenonnumber = (InputList) => {
    let primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283.293, 307, 311, 313]
    let Pieceslist = ['MT', 'WR', 'WN', 'WB', 'WQ', 'WK', 'WP', 'BR', 'BN', 'BB', 'BQ', 'BK', 'BP']
    let xenonnumber = 1
    let n1 = 0
    let n2 = 0
    let n3 = 0

    for (let j = 0; j < 8; j++) {
        for (let i = 0; i < 8; i++) {
            n1 = primeNumbers[i * j]
            n2 = Pieceslist.indexOf(InputList[j][i])
            n3 = n1 ** n2
            xenonnumber *= n3
        }
    }
    return xenonnumber
}

let toBoardLayout = (InputNumber) => {
    let primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283.293, 307, 311, 313]
    let Pieceslist = ['MT', 'WR', 'WN', 'WB', 'WQ', 'WK', 'WP', 'BR', 'BN', 'BB', 'BQ', 'BK', 'BP']
    let outputList = []
    let direction = []
    let n = 0
    let numcount = 0
    let piece = ''
    for (let i = 0; i < 64; i++) {
        n = primeNumbers[i]
        numcount = 0
        while (InputNumber % n === 0) {
            numcount += 1
            InputNumber /= n
        }
        piece = Pieceslist[numcount]
        direction.push(piece)
        if (i % 8 === 0 && i > 0) {
            outputList.push(direction)
            direction = []
        }
    }
    return outputList
}

let toCoOrdinates = (InputTuple) => {
    const letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
    return letters[(InputTuple[0])] + String(8 - InputTuple[1]);
};

let toTuple = (InputCoOrdinates) => {
    const letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
    return [Number(letters.indexOf(InputCoOrdinates[0])), 8 - Number(InputCoOrdinates[1])];
};

let toFEN = (InputList) => {        //this one script has to be run every time the script is run
    let output = '';
    let count = 0;
    for (let j = 0; j < 8; j++) {
        for (let i = 0; i < 8; i++) {
            count = 0;
            while (count + i < 8 && InputList[j][i + count] === 'MT') { count += 1 };      //handling when the square is empty, with the 'MT' marker
            if (InputList[j][i][0] === 'B') { output += InputList[j][i][1].toLocaleLowerCase(); }; // handling if its a black piece
            if (InputList[j][i][0] === 'W') { output += InputList[j][i][1]; };       //handling if its a white piece
            if (count > 0) {                                                      //handling if the square is empty as it ecodes more than oen squre at once, thus it'd have to skip over square that have already been checked
                i += (count - 1);
                output += count;
            };
        };
        output += '/';
    };
    return output.substring(0, output.length - 1);
};

let toDict = (InputList) => {
    let output = {};
    let outputString = '';
    let outputCoOrdinates = '';
    for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            if (!(InputList[j][i] === 'MT')) {
                outputString = InputList[j][i][0].toLocaleLowerCase() + InputList[j][i][1];
                outputCoOrdinates = toCoOrdinates([i, j])[0].toLocaleLowerCase() + toCoOrdinates([i, j])[1]
                output[outputCoOrdinates] = outputString;
            }
        };
    };
    return output;
};

let toUnicode = (InputString) => {
    let translationIndex = {
        'BK': '♔',
        'BQ': '♕',
        'BR': '♖',
        'BB': '♗',
        'BN': '♘',
        'BP': '♙',
        'WK': '♚',
        'WQ': '♛',
        'WR': '♜	',
        'WB': '♝	',
        'WN': '♞',
        'WP': '♟︎'
    }
    return translationIndex[InputString]
}

let listToString = (inputList) => {
    let outputList = []
    let outputString = ''
    let templist = []
    let s = ''
    let index = 0
    let chars = ['A','B','C','D','E','F','G','H','K','Q','N','M','R','P','T','W','0','1','2','3','4','5','6','7',',']
    let e = ''
    for (let i = 0; i < inputList.length; i++) {
        s = inputList[i][0] + inputList[i][1]
        if (inputList[i].length === 3) {
            templist = inputList[3]
            for (let count = 0; count < templist.length; count++) {
                s += templist[count]
            }
        }
        outputList.push(s)
    }

    for (let element = 0; element < outputList.length; element++) {
        for (let count = 0; count < outputList[element].length; count++) {
            index = chars.indexOf(outputList[element][count])
            if (index < 10) { e = '0' + String(index) }
            else { e = String(index) }
            outputString += e
        }
    }
    return outputString
}

function stringToList(InputString) {
    let chars=['A','B','C','D','E','F','G','H','K','Q','N','M','R','P','T','W','0','1','2','3','4','5','6','7',',']
    let outputstr=''
    let outputlist=[]
    let l=[]
    let templist = []
    let flag=-1
    let s=''
    let index=''
    for (let count = 0; count < InputString.length; count++) {
        if(count%2!=0) {
            index=InputString[count]
            outputstr+=chars[index]
        }
    }
    for (let count = 0; count < outputstr.length; count++) {
        if (outputlist[count]==',') {
            for (let i = 0; i < count-flag-1; i++) {
                s+=outputlist[i+flag]
                l.push(s)
            }
            flag=count
        }
    }
    outputlist=[]
    for (let count = 0; count < l.length; count++) {
        if (l[count].length==4){
            outputlist.push([l[count][0]+l[count][1],l[count][2]+l[count][3]])
        } else {
            for (let i = 5; i < l[count].length; i++) {
                if(i%2!=0) {
                    templist.push(l[count][i-1]+l[count][i])
                }
            }
            outputlist.push([l[count][0]+l[count][1],l[count][2]+l[count][3]],templist)
        }
    }
    return outputlist
}

export { toFEN, toDict, toTuple, toCoOrdinates, toBoardLayout, toXenonnumber, toUnicode, listToString, stringToList };