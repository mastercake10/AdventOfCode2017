use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};


// Day 6 part 1 + 2 solution in rust, tooks ~60 ms to solve

fn main() {
    let input = "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6";
    let splitted = input.split("\t");
    let mut banks = Vec::new();

    for s in splitted {
        banks.push(s.parse::<isize>().unwrap());
    }

    let mut previous_banks = Vec::new();
    let mut cys = 0;

    loop {
        cys += 1;
        previous_banks.push(calculate_hash(&banks));
        let mut max_bank_value = 0;
        let mut i = 0;
        {
            max_bank_value = *banks.iter().max().unwrap();
            i = banks.iter().position(|&r| r == max_bank_value).unwrap() as usize;
        }

        banks[i as usize] = 0;

        for _x in (0..max_bank_value).rev() {
            i = (i + 1) % banks.len();
            banks[i as usize] += 1
        }
        if previous_banks.contains(&calculate_hash(&banks)){
            break;
        }
    }

    println!("Output part1 = {}", cys);
    println!("Output part2 = {}", previous_banks.len() - previous_banks.iter().position(|&r| r == calculate_hash(&banks)).unwrap() as usize);

}
fn calculate_hash<T: Hash>(t: &T) -> u64 {
    let mut s = DefaultHasher::new();
    t.hash(&mut s);
    s.finish()
}
