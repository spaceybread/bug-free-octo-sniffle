fn main() {

    const  UPPER: usize = 1000;
    let mut list: [bool; UPPER + 1] = [true; UPPER + 1];

    let mut p_n: i32 = 2;

    while p_n.pow(2) < UPPER as i32 {
        if list[p_n as usize] == true {
            let mut i: i32 = p_n.pow(2);

            while i < UPPER as i32 + 1 {
                list[i as usize] = false;
                i += p_n;
            }
        }
        p_n += 1;
    }   

    for it in 1..UPPER as i32 {
        if list[it as usize] == true {
            println!("{it}");
        }
    }
}
