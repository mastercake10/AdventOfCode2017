use std::env;
use std::io::{self, BufReader};
use std::io::prelude::*;
use std::fs::File;
use std::time::Instant;


// Day 5 part 2 solution in rust; overhauled performance to a total of ~90ms

fn main() {
    let filename = "../inputs/day5.txt";
    let file = File::open(filename).expect("file not found");
    let buf_reader = BufReader::new(file);
    let lines = buf_reader.lines();

    let mut arr: [isize; 1200] = [0; 1200];
    let length: isize = arr.len() as isize;

    let mut cnt: usize = 0;
    for line in lines {
        arr[cnt] = line.unwrap().parse::<isize>().unwrap();
        cnt += 1usize;
    }
    // just for some time measurement
    let start = Instant::now();

    let mut idx: isize = 0;
    let mut steps: u32 = 0;

    loop {
        steps += 1u32;
        let data_at_idx: isize = arr[idx as usize] as isize;
        if data_at_idx >= 3 {
            arr[idx as usize] -= 1;
        } else{
            arr[idx as usize] += 1;
        }
        idx += data_at_idx;
        if idx >= length {
            println!("Part 2 solution = {}", steps as isize);
            break;
        }
    }

    // printing elapsed time
    let elapsed = start.elapsed();
    println!("Elapsed: {} ms",
            (elapsed.as_secs() * 1_000) + (elapsed.subsec_nanos() / 1_000_000) as u64);
}
