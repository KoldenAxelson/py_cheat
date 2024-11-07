mod cheatsheet;
mod highlighting;
mod manager;

use manager::CheatSheetManager;
use std::{env, process};

fn main() {
    let args: Vec<String> = env::args().collect();
    let manager = CheatSheetManager::new();

    let result = match args.len() {
        1 => {
            manager.show_available_sheets();
            Ok(())
        }
        2 => manager.show_full_sheet(&args[1]),
        3 => manager.show_section(&args[1], &args[2]),
        _ => Err("Usage: py_cheat [sheet_name] [section_number]".into()),
    };

    if let Err(e) = result {
        eprintln!("{}", manager.format_error(&e.to_string()));
        process::exit(1);
    }
}
