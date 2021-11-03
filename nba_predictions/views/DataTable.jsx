import * as React from "react";
import { styled } from "@mui/material/styles";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell, { tableCellClasses } from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";

const StyledTableCell = styled(TableCell)(({ theme }) => ({
  [`&.${tableCellClasses.head}`]: {
    backgroundColor: "#877ff4",
    color: "white"
  },
  [`&.${tableCellClasses.body}`]: {
    fontSize: 14
  }
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
  "&:nth-of-type(odd)": {
    backgroundColor: theme.palette.action.hover
  },
  // hide last border
  "&:last-child td, &:last-child th": {
    border: 0
  },
  "&:nth-child(n) th": {
    backgroundColor: "#877ff4",
    color: theme.palette.common.white,
    fontWeight: "bold"
  }
}));

function createData(stats, current, nextInLine, expected) {
  return { stats, current, nextInLine, expected };
}

const statistics = ["Points", "Assists", "Rebounds", "Blocks", "Steal"];

const rows = [
  createData( statistics[0], 159, 6.0, 24),
  createData( statistics[1], 237, 9.0, 37),
  createData( statistics[2], 237, 9.0, 37),
  createData( statistics[3], 12, 182.0, 130),
  createData( statistics[4], 94, 72.3, 110),
];

export default function CustomizedTables() {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 400 }} aria-label="customized table">
        <TableHead>
          <TableRow>
            <StyledTableCell style={{ opacity: "0.0" }}></StyledTableCell>
            <StyledTableCell align="center">Current</StyledTableCell>
            <StyledTableCell align="center">Goal</StyledTableCell>
            <StyledTableCell align="center">Expected games</StyledTableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <StyledTableRow key={row.stats}>
              <StyledTableCell component="th" scope="row">
                {row.stats}
              </StyledTableCell>
              <StyledTableCell align="center">{row.current}</StyledTableCell>
              <StyledTableCell align="center">{row.nextInLine}</StyledTableCell>
              <StyledTableCell align="center">{row.expected}</StyledTableCell>
            </StyledTableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}