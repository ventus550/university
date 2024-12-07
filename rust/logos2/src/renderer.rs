use svg::node::element::{Path};
use svg::node::element::path::Data; // Corrected import
use svg::Document;

pub fn render(lines: &Vec<(f64, f64, f64, f64)>) -> String {
    let mut data = Data::new();
    for &(x1, y1, x2, y2) in lines {
        data = data.move_to((x1, y1)).line_to((x2, y2));
    }

    let path = Path::new().set("fill", "none").set("stroke", "black").set("d", data);
    let document = Document::new().set("viewBox", (-200, -200, 400, 400)).add(path);

    document.to_string()
}
