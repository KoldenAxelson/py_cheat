const BASICS_PY: &str = include_str!("Basics.py");
const INTERMEDIATE_PY: &str = include_str!("Intermediate.py");
const ADVANCED_PY: &str = include_str!("Advanced.py");

use std::env;
use std::process;

#[derive(Debug)]
struct Section {
    title: String,
    content: String,
}

struct CheatSheet {
    sections: Vec<Section>,
}

fn main() {
    let args: Vec<String> = env::args().collect();

    match args.len() {
        1 => show_available_sheets(),
        2 => show_full_sheet(&args[1]),
        3 => show_section(&args[1], &args[2]),
        _ => {
            eprintln!("Usage: py_cheat [sheet_name] [section_number]");
            process::exit(1);
        }
    }
}

fn parse_content(content: &str) -> Result<CheatSheet, Box<dyn std::error::Error>> {
    let mut sections = Vec::new();
    let lines: Vec<&str> = content.lines().collect();
    let mut section_starts: Vec<usize> = Vec::new();

    // Find section starts
    for (i, line) in lines.iter().enumerate() {
        if line.starts_with("# ----") {
            if i + 1 < lines.len() && lines[i + 1].starts_with("# ") {
                if let Some(next_line) = lines.get(i + 1) {
                    if next_line
                        .trim_start_matches("# ")
                        .split_once(". ")
                        .is_some()
                    {
                        section_starts.push(i);
                    }
                }
            }
        }
    }

    // Process each section
    for i in 0..section_starts.len() {
        let start_idx = section_starts[i];
        let end_idx = if i < section_starts.len() - 1 {
            section_starts[i + 1]
        } else {
            lines.len()
        };

        if let Some(title_line) = lines.get(start_idx + 1) {
            if let Some((num, section_title)) = title_line.trim_start_matches("# ").split_once(". ")
            {
                if num.parse::<u32>().is_ok() {
                    let section_content = format!(
                        "{}\n{}\n{}\n{}",
                        lines[start_idx],
                        title_line,
                        lines[start_idx + 2],
                        lines[start_idx + 3..end_idx]
                            .iter()
                            .map(|&line| line.to_string())
                            .collect::<Vec<String>>()
                            .join("\n")
                    );

                    sections.push(Section {
                        title: section_title.to_string(),
                        content: section_content,
                    });
                }
            }
        }
    }

    Ok(CheatSheet { sections })
}

fn show_section(sheet_name: &str, section_number: &str) {
    if let Some(content) = get_sheet_content(sheet_name) {
        if let Ok(cheat_sheet) = parse_content(content) {
            if let Ok(section_idx) = section_number.parse::<usize>() {
                if section_idx > 0 && section_idx <= cheat_sheet.sections.len() {
                    let section = &cheat_sheet.sections[section_idx - 1];
                    print!("{}", section.content);
                } else {
                    eprintln!("Error: Invalid section number");
                    process::exit(1);
                }
            } else {
                eprintln!("Error: Section number must be a positive integer");
                process::exit(1);
            }
        }
    } else {
        eprintln!("Error: Could not find sheet {}", sheet_name);
        process::exit(1);
    }
}

fn get_sheet_content(name: &str) -> Option<&'static str> {
    match name {
        "Basics" => Some(BASICS_PY),
        "Intermediate" => Some(INTERMEDIATE_PY),
        "Advanced" => Some(ADVANCED_PY),
        _ => None,
    }
}

fn show_available_sheets() {
    let sheets = vec!["Basics", "Intermediate", "Advanced"];

    for sheet in sheets {
        if let Some(content) = get_sheet_content(sheet) {
            if let Ok(cheat_sheet) = parse_content(content) {
                println!("{}", sheet);
                for (i, section) in cheat_sheet.sections.iter().enumerate() {
                    let prefix = if i == cheat_sheet.sections.len() - 1 {
                        "└──"
                    } else {
                        "├──"
                    };
                    println!("{} {}. {}", prefix, i + 1, section.title);
                }
            }
        }
    }
}

fn show_full_sheet(sheet_name: &str) {
    if let Some(content) = get_sheet_content(sheet_name) {
        println!("{}", content);
    } else {
        eprintln!("Error: Could not find sheet {}", sheet_name);
        process::exit(1);
    }
}
