let toFEN = (InputList) => {        //this one script has to be run every time the script is run
    var output ='';
    var count =0;
    for (let j = 0; j < 8; j++) {
        for (let i = 0; i < 8; i++) {
            count=0
            while (count+i<8 && InputList[j][i+count][0]==='M') {count+=1}      //handling when the square is empty, with the 'MT' marker
            if (InputList[j][i][0]==='B')  {output += InputList[j][i][1].toLocaleLowerCase();}; // handling if its a black piece
            if (InputList[j][i][0]==='W') {output += InputList[j][i][1];}       //handling if its a white piece
            if (count>0) {                                                      //handling if the square is empty as it ecodes more than oen squre at once, thus it'd have to skip over square that have already been checked
                i+=count;
                output += count;
            }
        };
        output += '/';
    };
    return output.substring(0,output.length-1);
};

export default toFEN