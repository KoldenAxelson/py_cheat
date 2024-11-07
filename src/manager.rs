use crate::cheatsheet::CheatSheet;
use crate::highlighting::PythonHighlighter;
use std::error::Error;

const BASICS_PY: &str = include_str!("Basics.py");
const INTERMEDIATE_PY: &str = include_str!("Intermediate.py");
const ADVANCED_PY: &str = include_str!("Advanced.py");

pub struct CheatSheetManager {
    sheets: Vec<(&'static str, &'static str)>,
    highlighter: PythonHighlighter,
}

impl CheatSheetManager {
    pub fn new() -> Self {
        let sheets = vec![
            ("Basics", BASICS_PY),
            ("Intermediate", INTERMEDIATE_PY),
            ("Advanced", ADVANCED_PY),
        ];

        Self {
            sheets,
            highlighter: PythonHighlighter::new(),
        }
    }

    fn get_sheet_content(&self, name: &str) -> Option<&'static str> {
        self.sheets
            .iter()
            .find(|(sheet_name, _)| *sheet_name == name)
            .map(|(_, content)| *content)
    }

    pub fn show_available_sheets(&self) {
        for (sheet_name, content) in &self.sheets {
            if let Ok(cheat_sheet) = CheatSheet::parse(content) {
                println!("\n{}", self.highlighter.format_header(sheet_name, true));
                self.print_sections(&cheat_sheet.sections);
            }
        }
    }

    fn print_sections(&self, sections: &[crate::cheatsheet::Section]) {
        for (i, section) in sections.iter().enumerate() {
            let prefix = if i == sections.len() - 1 {
                "└──"
            } else {
                "├──"
            };
            let header = format!("{} {}. {}", prefix, i + 1, section.title);
            println!("{}", self.highlighter.format_header(&header, false));
        }
    }

    pub fn show_section(
        &self,
        sheet_name: &str,
        section_number: &str,
    ) -> Result<(), Box<dyn Error>> {
        let content = self
            .get_sheet_content(sheet_name)
            .ok_or_else(|| format!("Could not find sheet {}", sheet_name))?;

        let cheat_sheet = CheatSheet::parse(content)?;
        let section_idx = section_number
            .parse::<usize>()
            .map_err(|_| "Section number must be a positive integer")?;

        if section_idx == 0 || section_idx > cheat_sheet.sections.len() {
            return Err("Invalid section number".into());
        }

        print!(
            "{}",
            self.highlighter
                .highlight(&cheat_sheet.sections[section_idx - 1].content)
        );
        Ok(())
    }

    pub fn show_full_sheet(&self, sheet_name: &str) -> Result<(), Box<dyn Error>> {
        let content = self
            .get_sheet_content(sheet_name)
            .ok_or_else(|| format!("Could not find sheet {}", sheet_name))?;

        println!("{}", self.highlighter.highlight(content));
        Ok(())
    }

    pub fn format_error(&self, error: &str) -> String {
        self.highlighter.format_error(error)
    }
}
