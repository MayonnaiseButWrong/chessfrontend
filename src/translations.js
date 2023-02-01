let toXenonnumber = (InputList) => {
    let primeNumbers=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283.293,307,311,313]
    let Pieceslist=['MT','WR','WN','WB','WQ','WK','WP','BR','BN','BB','BQ','BK','BP']
    let xenonnumber=1
    let n1=0
    let n2=0
    let n3=0

    for (let j = 0; j < 8; j++) {
        for (let i = 0; i < 8; i++) {
            n1=primeNumbers[i*j]
            n2=Pieceslist.indexOf(InputList[j][i])
            n3=n1**n2
            xenonnumber*=n3
        }
    }
    return xenonnumber
}

let toBoardLayout = (InputNumber) => {
    let primeNumbers=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283.293,307,311,313]
    let Pieceslist=['MT','WR','WN','WB','WQ','WK','WP','BR','BN','BB','BQ','BK','BP']
    let outputList=[]
    let direction=[]
    let n=0
    let numcount=0
    let piece=''
    for (let i = 0; i < 64; i++) {
        n=primeNumbers[i]
        numcount=0
        while (InputNumber%n==0) {
            numcount+=1
            InputNumber/n
        }
        piece=Pieceslist[numcount]
        direction.push(piece)
        if (i%8==0&&i>0) {
            outputList.push(direction)
            direction=[]
        }
    }
    return outputList
}

let toCoOrdinates = (InputTuple) => {
    const letters=['A','B','C','D','E','F','G','H'];
    return letters[(InputTuple[0])]+String(8-InputTuple[1]);
};

let toTuple = (InputCoOrdinates) => {
    const letters=['A','B','C','D','E','F','G','H'];
    return [Number(letters.indexOf(InputCoOrdinates[0])),8-Number(InputCoOrdinates[1])];
};

let toFEN = (InputList) => {        //this one script has to be run every time the script is run
    let output ='';
    let count =0;
    for (let j = 0; j < 8; j++) {
        for (let i = 0; i < 8; i++) {
            count=0;
            while (count+i<8 && InputList[j][i+count]==='MT') {count+=1};      //handling when the square is empty, with the 'MT' marker
            if (InputList[j][i][0]==='B')  {output += InputList[j][i][1].toLocaleLowerCase();}; // handling if its a black piece
            if (InputList[j][i][0]==='W') {output += InputList[j][i][1];};       //handling if its a white piece
            if (count>0) {                                                      //handling if the square is empty as it ecodes more than oen squre at once, thus it'd have to skip over square that have already been checked
                i+=(count-1);
                output += count;
            };
        };
        output += '/';
    };
    return output.substring(0,output.length-1);
};

let toDict = (InputList) => {
    let output = new Object();
    let outputString = '';
    let outputCoOrdinates='';
    for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            if (!(InputList[j][i]==='MT')) {
                outputString=InputList[j][i][0].toLocaleLowerCase()+InputList[j][i][1];
                outputCoOrdinates=toCoOrdinates([i,j])[0].toLocaleLowerCase()+toCoOrdinates([i,j])[1]
                output[outputCoOrdinates]=outputString;
            }
        };
    };
    return output;
};

export {toFEN,toDict,toTuple,toCoOrdinates,toBoardLayout,toXenonnumber};