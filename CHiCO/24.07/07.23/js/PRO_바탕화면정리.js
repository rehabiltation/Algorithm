function solution(wallpaper) {
  let min_x= 999, min_y= 999, max_x= -999, max_y = -999
  for (let i = 0; i < wallpaper.length; i ++ ){
    for (let j = 0; j < wallpaper[i].length; j ++){
      if (wallpaper[i][j] === '#'){
        if (min_x > j){
          min_x = j
        }
        if (min_y > i){
          min_y = i
        }
        if (max_x < j){
          max_x = j
        }
        if (max_y < i){
          max_y = i
        }
      }
    }
  }
  
  return [min_y,min_x,max_y+1,max_x+1];
}