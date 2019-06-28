use std::io; // like python import

// fn --> def
fn main() {
    println!("Guess the number!");

    println!("Please input your guess.");

    // default is immutable, python deafult is mut
    // String --> string class
    // String::new() --> String.new() (python)
    // the new fuction creats a new empty string
    let mut guess = String::new(); // mutable

    // directly use io because the first line import stdio
    // read_line fuction,takes string as argument
    // & represents reference, access to data without copy
    io::stdin().read_line(&mut guess)
    	.expect("Failed to read line");

    println!("Guess the number!");

}
