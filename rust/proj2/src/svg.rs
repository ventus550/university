use crate::interpreter::Turtle;
use svg::Document;
use svg::node::element::Path;
use svg::node::element::path::Data;

pub fn save_to_svg(turtle: &Turtle, file_name: &str) {
    let mut data = Data::new();

    for &(x1, y1, x2, y2) in &turtle.paths {
		println!("Move {} {} {} {}", x1, y1, x2, y2);
        data = data.move_to((x1, y1)).line_to((x2, y2));
    }

    let path = Path::new().set("fill", "none").set("stroke", "black").set("d", data);
    let document = Document::new().set("viewBox", (0, 0, 500, 500)).add(path);

    svg::save(file_name, &document).unwrap();
}
