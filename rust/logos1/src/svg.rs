use svg::node::element::{Path, path::Data};
use svg::Document;

pub fn save_as_svg(path: &[(f64, f64)], filename: &str) {
    let mut data = Data::new().move_to(path[0]);
    for &(x, y) in &path[1..] {
        data = data.line_to((x, y));
    }

    let path = Path::new().set("fill", "none").set("stroke", "black").set("d", data);
    let document = Document::new().set("viewBox", (-200, -200, 400, 400)).add(path);
    svg::save(filename, &document).unwrap();
}
